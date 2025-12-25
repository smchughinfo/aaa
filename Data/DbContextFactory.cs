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
            var host = Environment.GetEnvironmentVariable("aaa_neon_db_host");
            var database = Environment.GetEnvironmentVariable("aaa_neon_db_database");
            var username = Environment.GetEnvironmentVariable("aaa_neon_db_username");
            var password = Environment.GetEnvironmentVariable("aaa_neon_db_password");
            optionsBuilder.UseNpgsql(
                $"Host={host};Database={database};Username={username};Password={password};SSL Mode=Require",
                o => o.UseVector()
            );

            return new DbContext(optionsBuilder.Options);
        }
    }
}