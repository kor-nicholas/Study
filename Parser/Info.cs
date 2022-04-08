using HtmlAgilityPack;
using RandomUserAgent; // Nuget(RandomUserAgent)

namespace Study.Parser
{
    public class Info
    {
        private async void Method()
        {
            //var link = @"https://www.kufar.by/l";

            HtmlWeb web = new HtmlWeb();

            await web.UserAgent = RandomUa.RandomUserAgent;
            //var htmlDoc = await web.LoadFromWebAsync(link);
            //htmlDoc.Save("D:\\Programming\\C#\\Study\\Study.Test\\test.html");

            // ----------------------------------------------------------------------------------------------------------------

            HtmlDocument doc = new HtmlDocument();
            //doc.Load("test.html"); // загрузить из файла
            //doc.Save("test.html"); // сохранить в html файл (если были какие-то изменения)
            doc.Load("D:\\Programming\\C#\\Study\\Study.Test\\test.html");

            // ----------------------------------------------------------------------------------------------------------------

            //var cards = htmlDoc.DocumentNode.Descendants().Where(test => test.HasClass("kf-Kqo-0e037"))
            //    .Select(test => test.GetAttributeValue("href", "не нашел")); // достает по классу и атрибуту
            // аналогия на Python: soup.find_all('href', class_='kf-Kqo-0e037')
            // Свойство InnerText - достает текст

            var cards = doc.DocumentNode.Descendants().Where(test => test.HasClass("kf-Kqo-0e037"));

            foreach (var card in cards)
            {
                string href = card.GetAttributeValue("href", "Не удалось найти атрибут href").Trim();
                string title = card.SelectSingleNode(".//h3").InnerText.Trim();
                string price = card.SelectSingleNode(".//p/span").InnerText.Trim();
                string category = "";

                Console.WriteLine($"titlle: {title}\nprice: {price}\nhref: {href}\n");

            }

        }


    }
}



