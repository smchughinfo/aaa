using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Data.Entities
{
    [Table("markets")]
    public class Market
    {
        [Key]
        [Column("id")]
        public string Id { get; set; }

        [Column("event_id")]
        public string EventId { get; set; }

        [Column("question")]
        public string Question { get; set; }

        [Column("best_bid")]
        public decimal BestBid { get; set; }

        [Column("best_ask")]
        public decimal BestAsk { get; set; }

        [Column("end_date")]
        public DateTime EndDate { get; set; }

        [Column("outcomes")]
        public string Outcomes { get; set; } // Stored as JSONB in Postgres

        [Column("platform")]
        public string Platform { get; set; } // "Kalshi" or "Polymarket"

        [Column("last_updated")]
        public DateTime LastUpdated { get; set; }

        // For later when you add embeddings:
        // [Column("embedding")]
        // public float[] Embedding { get; set; }
    }
}