using HtmlAgilityPack;
using Newtonsoft.Json.Linq;
using ParserBot.Abstractions;
using ParserBot.Models;
using RandomUserAgent;

namespace ParserBot.Services
{
    public class ParserService : IParserService
    {
        private readonly ILogger _logger;
        private List<Car> _cars;
        private List<Vacancy> _vacancies;
        private int i;
        private int j;

        public ParserService(ILogger<ParserService> logger)
        {
            i = int.Parse(File.ReadAllText("D:\\Programming\\C#\\Telegram Bots\\ParserBot\\ParserBot\\Files\\settingsCars.txt"));
            j = int.Parse(File.ReadAllText("D:\\Programming\\C#\\Telegram Bots\\ParserBot\\ParserBot\\Files\\settingsVacancy.txt"));

            _logger = logger;
        }

        /// <summary>
        /// Спарсит все объявления машин со страницы
        /// </summary>
        /// <param name="link"></param>
        /// <returns>Коллекция объявлений</returns>
        public async Task<bool> ParseCarAdds(string link)
        {
            _cars = new List<Car>();

            string json = await SaveHtmlAndSave(link, $"D:\\Programming\\C#\\Telegram Bots\\ParserBot\\ParserBot\\Files\\html\\car{i += 1}.html");

            JObject jObject = JObject.Parse(json);

            var ads = jObject["props"]["initialState"]["listing"]["ads"];

            int id = 1;
            foreach (var add in ads)
            {
                string title = add["subject"].ToString();
                string href = add["ad_link"].ToString();
                string price = $"{ int.Parse((string)add["price_byn"]) / 100 }р. | { int.Parse((string)add["price_usd"]) / 100}$";
                string publicDate = add["list_time"].ToString();
                string city = "";
                string year = "";
                string mileage = ""; // пробег
                string engine = ""; // бензин/дизель
                string capacity = ""; // объем
                string gearbox = ""; // коробка
                string type = ""; // кузов
                string drive = ""; // привод
                string color = "";
                string desc = "";
                
                string photo = "";
                try
                {
                    Int64 photoId = Int64.Parse(add["images"][0]["id"].ToString());
                    double subPhotoId = photoId / 100000000;

                    if (subPhotoId < 10)
                    {
                        photo = $"https://yams.kufar.by/api/v1/kufar-ads/images/{Convert.ToString(subPhotoId / 100.0).Remove(0, 2)}/{Convert.ToString(photoId / 10000000000.0).Remove(0, 2)}.jpg?rule=list_thumbs_2x";
                        continue;
                    }

                    photo = $"https://yams.kufar.by/api/v1/kufar-ads/images/{subPhotoId}/{photoId}.jpg?rule=list_thumbs_2x";
                }
                catch (ArgumentOutOfRangeException)
                {
                    _logger.LogCritical("Может выскочить ошибка, связання с кодировкой"); // https://thumbs.dreamstime.com/z/хлеб-193944749.jpg
                    photo = "https://thumbs.dreamstime.com/z/хлеб-193944749.jpg";
                }

                var adParameters = add["ad_parameters"];

                foreach (var parameter in adParameters)
                {
                    switch (parameter["p"].ToString())
                    {
                        case "region":
                            city = parameter["vl"].ToString();
                            city += ", ";
                            break;
                        case "area":
                            city += parameter["vl"];
                            break;
                        case "regdate":
                            year = parameter["vl"].ToString();
                            break;
                        case "mileage":
                            mileage = parameter["vl"].ToString();
                            break;
                        case "cars_engine":
                            engine = parameter["vl"].ToString();
                            break;
                        case "cars_capacity":
                            capacity = parameter["vl"].ToString();
                            break;
                        case "cars_gearbox":
                            gearbox = parameter["vl"].ToString();
                            break;
                        case "cars_type":
                            type = parameter["vl"].ToString();
                            break;
                        case "cars_drive":
                            drive = parameter["vl"].ToString();
                            break;
                        case "cars_color":
                            color = parameter["vl"].ToString();
                            break;
                    }
                }

                desc = $"Кузов: {type}\n" +
                    $"Рiк випуску: {year}\n" +
                    $"Тип двигуна: {engine}\n" +
                    $"Об'єм двигуна: {capacity}\n" +
                    $"Коробка передач: {gearbox}\n" +
                    $"Пробiг: {mileage}\n" +
                    $"Привод: {drive}\n" +
                    $"Колiр: {color}";

                _cars.Add(new Car
                {
                    Id = id++,
                    Title = title,
                    Description = desc,
                    Price = price,
                    City = city,
                    PublicationDate = publicDate,
                    Photo = photo,
                    Link = href
                });

                _logger.LogInformation($"[Car] Title: {title}\n" +
                    $"Desc: {desc}\n" +
                    $"Price: {price}\n" +
                    $"City: {city}\n" +
                    $"Publication Date: {publicDate}\n" +
                    $"Photo: {photo}\n" +
                    $"Link: {href}\n");

                await Task.Delay(1000);
            }

            SaveListAddsInJson($"D:\\Programming\\C#\\Telegram Bots\\ParserBot\\ParserBot\\Files\\json\\car{i}.json");

            return true;
        }

        /// <summary>
        /// Спарсит все объявления вакансий со страницы
        /// </summary>
        /// <param name="link"></param>
        /// <returns>Коллекция объявлений</returns>
        public async Task<bool> ParseVacancyAddsAsync(string link)
        {
            _vacancies = new List<Vacancy>();

            string json = await SaveHtmlAndSave(link ,$"D:\\Programming\\C#\\Telegram Bots\\ParserBot\\ParserBot\\Files\\html\\vacancy{j += 1}.html");

            JObject jObject = JObject.Parse(json);

            var ads = jObject["props"]["initialState"]["listing"]["ads"];

            int id = 1;
            foreach (var add in ads)
            {
                string title = add["subject"].ToString();
                string href = add["ad_link"].ToString();
                string salary = $"{ int.Parse((string)add["price_byn"]) / 100 }р. | { int.Parse((string)add["price_usd"]) / 100}$";
                string publicDate = add["list_time"].ToString();
                string city = "";
                string jobSegment = "";
                string expirience = "";
                string jobTime = "";

                string photo = "";
                try
                {
                    Int64 photoId = Int64.Parse(add["images"][0]["id"].ToString());
                    double subPhotoId = photoId / 100000000;

                    if (subPhotoId < 10)
                    {
                        photo = $"https://yams.kufar.by/api/v1/kufar-ads/images/{Convert.ToString(subPhotoId / 100.0).Remove(0, 2)}/{Convert.ToString(photoId / 10000000000.0).Remove(0, 2)}.jpg?rule=list_thumbs_2x";
                        continue;
                    }

                    photo = $"https://yams.kufar.by/api/v1/kufar-ads/images/{subPhotoId}/{photoId}.jpg?rule=list_thumbs_2x";
                }
                catch (ArgumentOutOfRangeException)
                {
                    photo = "https://cs12.pikabu.ru/post_img/big/2022/03/03/7/164630201911556038.jpg";
                }

                var adParameters = add["ad_parameters"];

                foreach (var parameter in adParameters)
                {
                    switch (parameter["p"].ToString())
                    {
                        case "region":
                            city = parameter["vl"].ToString();
                            city += ", ";
                            break;
                        case "area":
                            city += parameter["vl"];
                            break;
                        case "jobs_segment":
                            jobSegment = parameter["vl"].ToString();
                            break;
                        case "jobs_experience":
                            expirience = parameter["vl"].ToString();
                            break;
                        case "jobs_type":
                            jobTime = parameter["vl"].ToString();
                            break;
                    }
                }

                _vacancies.Add(new Vacancy
                {
                    Id = id++,
                    Title = title,
                    JobSegment = jobSegment,
                    JobTime = jobTime,
                    Expirience = expirience,
                    Salary = salary,
                    City = city,
                    PublicationDate = publicDate,
                    Photo = photo,
                    Link = href
                });

                _logger.LogInformation($"[Vacancy] Title: {title}\n" +
                    $"Link: {href}\n" +
                    $"City: {city}\n" +
                    $"Price: {salary}\n" +
                    $"PublicationDate: {publicDate}\n" +
                    $"Photo: {photo}\n" +
                    $"Sfera Deyatelnosti: {jobSegment}\n" +
                    $"Expirience: {expirience}\n" +
                    $"Job Time: {jobTime}\n");

                await Task.Delay(1000);
            }

            SaveListAddsInJson($"D:\\Programming\\C#\\Telegram Bots\\ParserBot\\ParserBot\\Files\\json\\vacancy{j}.json");

            return true;

        }

        /// <summary>
        /// Сохранить коллекцию объявлений в json
        /// </summary>
        /// <param name="adds"></param>
        /// <param name="path"></param>
        /// <returns></returns>
        private bool SaveListAddsInJson(string path)
        {
            try
            {
                if (path.Contains("car"))
                {
                    File.WriteAllText($"{path}", Newtonsoft.Json.JsonConvert.SerializeObject(_cars));
                    File.WriteAllText("D:\\Programming\\C#\\Telegram Bots\\ParserBot\\ParserBot\\Files\\settingsCars.txt", $"{i}");
                    _logger.LogInformation($"[SaveListAddsInJson] settingsCar.txt rewrite to {i}");
                }
                else if (path.Contains("vacancy"))
                {
                    File.WriteAllText($"{path}", Newtonsoft.Json.JsonConvert.SerializeObject(_vacancies));
                    File.WriteAllText("D:\\Programming\\C#\\Telegram Bots\\ParserBot\\ParserBot\\Files\\settingsVacancy.txt", $"{j}");
                    _logger.LogInformation($"[SaveListAddsInJson] settingsVacancy rewrite to {j}");
                }
                else
                {
                    _logger.LogCritical($"[SaveListAddsInJson] Category isn't correct");
                }

                _logger.LogInformation($"[SaveListAddsInJson] [{path}] Saved Json file");
                return true;
            }
            catch (Exception e)
            {
                _logger.LogError($"[SaveListAddsInJson] [{path}] {e.Message}");
                return false;
            }
        }

        /// <summary>
        /// Сохранить html-страницу и json в файлы 
        /// </summary>
        /// <param name="link"></param>
        /// <param name="path"></param>
        /// <returns>json</returns>
        private async Task<string> SaveHtmlAndSave(string link, string path)
        {
            HtmlWeb web = new HtmlWeb();

            web.UserAgent = RandomUa.RandomUserAgent;
            var htmlDoc = await web.LoadFromWebAsync(link);
            htmlDoc.Save(path);
            _logger.LogInformation($"[SaveHtmlAndSave] Html-page saved");

//-----------------------------------------------------------------------------------------------------------------------------------------------

            var json = htmlDoc.DocumentNode.SelectSingleNode("//script[@id='__NEXT_DATA__']").InnerText.Trim();
            path = path.Replace("html", "json");
            File.WriteAllText(path, json);
            _logger.LogInformation("[SaveHtmlAndJson] Json saved");

            return json;
        }

        




        #region Help

        //private class Comment
        //{
        //    private void Method()
        //    {
        //        //var href = @"https://severlesgroup.ru/pilomaterialy/doska-obreznayal";

        //        HtmlWeb web = new HtmlWeb();

        //        web.UserAgent = RandomUa.RandomUserAgent;
        //        //var htmlDoc = await web.LoadFromWebAsync(href);
        //        //htmlDoc.Save("D:\\Programming\\C#\\Study\\Study.Test\\test.html");

        //        // ----------------------------------------------------------------------------------------------------------------

        //        HtmlDocument doc = new HtmlDocument();
        //        //doc.Load("test.html"); // загрузить из файла
        //        //doc.Save("test.html"); // сохранить в html файл (если были какие-то изменения)
        //        doc.Load("D:\\Programming\\C#\\Study\\Study.Test\\test.html");

        //    }

        #endregion











    }
}
