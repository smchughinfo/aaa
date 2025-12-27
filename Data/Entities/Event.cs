using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Text;

namespace Data.Entities
{
    [Table("events")]
    public class Event
    {
        [Key]
        [Column("id")]
        public string Id { get; set; }

        // For later when you add embeddings:
        [Column("embedding")]
        public float[]? Embedding { get; set; }

        [Column("question")]
        public string? Question { get; set; }
    }
}
