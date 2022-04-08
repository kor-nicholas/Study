// IEnumerable - generic (� <>) ������������ ��� List �������� (���� �� ��������, ������� ����� �������� � foreach)

// ����� ��� ������������� -> public IEnumerable<CityOuput> GetAllCities() return ... .ToList()
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