using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace HelloWorldWebAPI_Cat_
{
    public class Linq
    {
        //private List<Cat> lists = DbCats.lists;

        //public List<Cat> Test1(int id)
        //{
        //    var selectedCats = from cat in lists // в переменную Cat присваивается каждый объект lists 
        //                       where cat.Id == id // если Id объекта Cat == id которое пришло параметром - ... (bool)
        //                       orderby cat.Name // сортировка по имени (просто указываем то, по чем сортируем)
        //                       select cat; // это значение мы заносим в результат, а если нет - пропускаем и идем дальше по всем остальным объектам коллекции

        //    return selectedCats.ToList();
        //}

        //public List<Cat> Test2()
        //{
        //    var result = lists.OrderBy(lists => lists.Name); // сортировка по имени по убыванию

        //    result.ThenByDescending(lists => lists.Id); // если в прошлой сортировке есть одинаковые имена, то они сортируются уже по Id по возрастанию

        //    var result2 = from cat in lists select cat;
        //    result2.OrderBy(result2 => result2.Name).ThenByDescending(result2 => result2.Id); // тоже самое что и выше, просто сделано другим способом

        //    //lists = lists.OrderBy(lists => lists.Name).ThenByDescending(lists => lists.Id).ToList(); // все тоже самое в одну строчку, но lists перезаписывается

        //    return result.ToList();
        //}

        //public int Test3()
        //{
        //    int sumIds = lists.Sum(lists => lists.Id); // сумма всех Id

        //    var Ids = from cat in lists select cat.Id;
        //    Ids.Sum(); // другой вариант суммы всех Id

        //    return sumIds;
        //}

        //public void Test4()
        //{
        //    //try
        //    //{
        //    //    return Ok(DbCats.lists.Single(cat => cat.Id == id)); - возвращается ссылка на один оригинальный объект (который можно изменять)
        //    //}
        //    //catch (Exception)
        //    //{
        //    //    return BadRequest();
        //    //}

        //    //return Ok(from cat in DbCats.lists where cat.Id == id select cat); - возвращается List ссылок на оригинальные объекты (которые можно изменять)

        //    //foreach (var item in DbCats.lists)
        //    //    if (item.Id == id)
        //    //        return Ok(item);
        //}

        //[HttpGet("linq")]
        //public IActionResult GetTestLinq(int id)
        //{
        //    Linq linq = new Linq();

        //    switch (id)
        //    {
        //        case 11:
        //            return Ok(linq.Test1(1));

        //        case 12:
        //            return Ok(linq.Test1(2));

        //        case 2:
        //            return Ok(linq.Test2());

        //        case 3:
        //            return Ok(linq.Test3());

        //        default:
        //            return BadRequest();
        //    }
        //}
    }
}
