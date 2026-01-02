using Data.Entities;
using Microsoft.EntityFrameworkCore;
using Pgvector.EntityFrameworkCore;

namespace Data
{
    public class DbContext : Microsoft.EntityFrameworkCore.DbContext
    {
        public DbContext(DbContextOptions<DbContext> options)
            : base(options)
        {
        }

        public DbSet<Market> Markets { get; set; }
        public DbSet<Event> Events { get; set; }
        public DbSet<Comparisons> Comparisons{ get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);

            modelBuilder.HasPostgresExtension("vector");

            modelBuilder.Entity<Market>(entity =>
            {
                entity.HasKey(e => e.Id);
                entity.Property(e => e.Outcomes)
                    .HasColumnType("jsonb");
            });

            modelBuilder.Entity<Event>(entity =>
            {
                entity.HasKey(e => e.Id);
                entity.Property(e => e.Embedding)
                    .HasColumnType("vector(1536)");
            });
        }
    }
}