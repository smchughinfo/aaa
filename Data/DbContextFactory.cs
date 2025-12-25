using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Design;

namespace Data
{
    public class DbContextFactory : IDesignTimeDbContextFactory<DbContext>
    {
        public DbContext CreateDbContext(string[] args)
        {
            var optionsBuilder = new DbContextOptionsBuilder<DbContext>();

            // Hardcode connection string for migrations only
            optionsBuilder.UseNpgsql(
                Environment.GetEnvironmentVariable("aaa_neon_db"),
                o => o.UseVector()
            );

            return new DbContext(optionsBuilder.Options);
        }
    }
}