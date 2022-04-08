// IEnumerable - generic (с <>) предназначен для List объектов (лиюо же объектов, которые могут работать с foreach)

// варик без асинхронности -> public IEnumerable<CityOuput> GetAllCities() return ... .ToList()
public async Task<IEnumerable<CityOutput>> GetAllCitiesAsync()
{
    var result = await _context.Cities
        .Select(city => new CityOutput
        {
            CityId = city.CityId,
            CityName = city.CityName
        })
        .ToListAsync();

    return result;
}