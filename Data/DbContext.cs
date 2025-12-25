using Data.Entities;
using Microsoft.EntityFrameworkCore;

namespace Data
{
    public class DbContext : Microsoft.EntityFrameworkCore.DbContext
    {
        public DbContext(DbContextOptions<DbContext> options)
            : base(options)
        {
        }

        public DbSet<Market> Markets { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);

            modelBuilder.Entity<Market>(entity =>
            {
                entity.HasKey(e => e.Id);

                entity.Property(e => e.Outcomes)
                    .HasColumnType("jsonb"); // Postgres JSONB type

                // If you add embeddings later:
                // entity.Property(e => e.Embedding)
                //     .HasColumnType("vector(1536)");
            });
        }
    }
}