using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Text;
using Microsoft.EntityFrameworkCore;

namespace Data.Entities
{
    [Table("comparisons")]
    [PrimaryKey(nameof(Market_1_Id), nameof(Market_2_Id))]
    public class Comparisons
    {
        [Column("market_1_id")]
        [ForeignKey("Market1")]
        public string Market_1_Id { get; set; }

        [Column("market_2_id")]
        [ForeignKey("Market2")]
        public string Market_2_Id { get; set; }

        [Column("market_1_canonical_similarity")]
        public double Market_1_Canonical_Similarity { get; set; }
        [Column("market_2_canonical_similarity")]
        public double Market_2_Canonical_Similarity { get; set; }

        [Column("comparable")]
        public bool? Comparable { get; set; }

        // Navigation properties
        public Market Market1 { get; set; }
        public Market Market2 { get; set; }
    }
}
