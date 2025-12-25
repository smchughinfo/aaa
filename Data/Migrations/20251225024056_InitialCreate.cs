using System;
using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Data.Migrations
{
    /// <inheritdoc />
    public partial class InitialCreate : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "markets",
                columns: table => new
                {
                    id = table.Column<string>(type: "text", nullable: false),
                    event_id = table.Column<string>(type: "text", nullable: false),
                    question = table.Column<string>(type: "text", nullable: false),
                    best_bid = table.Column<decimal>(type: "numeric", nullable: false),
                    best_ask = table.Column<decimal>(type: "numeric", nullable: false),
                    end_date = table.Column<DateTime>(type: "timestamp with time zone", nullable: false),
                    outcomes = table.Column<string>(type: "jsonb", nullable: false),
                    platform = table.Column<string>(type: "text", nullable: false),
                    last_updated = table.Column<DateTime>(type: "timestamp with time zone", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_markets", x => x.id);
                });
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "markets");
        }
    }
}
