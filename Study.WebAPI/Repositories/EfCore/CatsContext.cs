using Cats.DAL.Models;
using Microsoft.EntityFrameworkCore;

namespace Cats.DAL.Repositories.EfCore
{
    public class CatsContext : DbContext
    {
        public CatsContext(DbContextOptions<CatsContext> options) : base(options) { }

        public DbSet<Cat> Cats { get; set; }
    }
}
