using Newtonsoft.Json;

// https://jsonplaceholder.typicode.com/ - фейк API (кидает левые данные, для теста)

#region Get

using (var client = new HttpClient())
{
    var endpoint = new Uri("https://jsonplaceholder.typicode.com/posts");
    var result = client.GetAsync(endpoint).Result;
    var json = result.Content.ReadAsStringAsync().Result;

    var values = JsonConvert.DeserializeObject<List<Dictionary<string, object>>>(json);

    // posts
    foreach (var value in values)
    {
        Console.WriteLine($"\nUserId: {value["userId"]}\nId: {value["id"]}\nTitle: {value["title"]}");
    }

    // users
    foreach (var item in values)
    {
        Console.WriteLine($"\n'Address': {item["address"]}");

        var json2 = JsonConvert.SerializeObject(item["address"]);
        var value = JsonConvert.DeserializeObject<Dictionary<string, object>>(json2);

        Console.WriteLine($"\n'Geo': {value["geo"]}");
    }

    Console.WriteLine($"\nGet json: {json}\n");
    Console.WriteLine($"\nGet values: {values}");

    // 2 вариант - dynamic
    dynamic d = JsonConvert.DeserializeObject(json);
    var name = d.name; // если уверен что есть поле name, то можно так
}

#endregion

#region Post

using (var client = new HttpClient())
{
    var endpoint = new Uri("https://jsonplaceholder.typicode.com/posts");
    Model model = new Model
    {
        Id = 1,
        Name = "Test"
    };
    var modelJson = JsonConvert.SerializeObject(model);
    var payload = new StringContent(modelJson, System.Text.Encoding.UTF8, "application/json");
    var result = client.PostAsync(endpoint, payload).Result.Content.ReadAsStringAsync().Result;
    model = JsonConvert.DeserializeObject<Model>(result);

    Console.WriteLine($"Post result: {result}\n\nId = {model.Id}");
}

#endregion

#region Json

//{
//    "id": 1,
//    "name": "Leanne Graham",
//    "username": "Bret",
//    "email": "Sincere@april.biz",
//    "address": {
//        "street": "Kulas Light",
//      "suite": "Apt. 556",
//      "city": "Gwenborough",
//      "zipcode": "92998-3874",
//      "geo": {
//            "lat": "-37.3159",
//        "lng": "81.1496"
//      }
//    },
//    "phone": "1-770-736-8031 x56442",
//    "website": "hildegard.org",
//    "company": {
//        "name": "Romaguera-Crona",
//      "catchPhrase": "Multi-layered client-server neural-net",
//      "bs": "harness real-time e-markets"
//    }
//},

#endregion

#region Template KudaGo

/// <summary>
/// В репозитории содержится функционал для получения информации из сервиса KudaGo.
/// </summary>
public class KudaGoRepository : IKudaGoRepository
{
    private string ApiUrl = "https://kudago.com/public-api/";
    private string ApiVersion = "v1.4";

    public KudaGoRepository()
    {
    }

    /// <summary>
    /// Получение списка всех доступных городов.
    /// </summary>
    /// <returns> Список доступных городов. </returns>
    public async Task<IEnumerable<KudaGoCitiesOutput>> GetAllAvailableCitiesAsync()
    {
        using (HttpClient client = new HttpClient())
        {

            var response = await client.GetAsync(ApiUrl + ApiVersion + "/locations/?lang=ru");


            if (response.IsSuccessStatusCode)
            {
                return await response.Content.ReadAsAsync<IEnumerable<KudaGoCitiesOutput>>();
            }
            else if (response.StatusCode.Equals(HttpStatusCode.NotFound))
            {
                throw new NotFoundException("KudaGo Api locations notfound result code");
            }
            else
            {
                throw new Exception("KudaGo Api locations " + response.StatusCode.ToString() + " result code");
            }
        }
    }
}

#endregion

public class Model
{
    public int Id { get; set; }
    public string Name { get; set; }
}
