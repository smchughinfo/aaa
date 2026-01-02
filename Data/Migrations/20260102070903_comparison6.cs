using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Data.Migrations
{
    /// <inheritdoc />
    public partial class comparison6 : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.RenameColumn(
                name: "canonical_similarity",
                table: "comparisons",
                newName: "market_2_canonical_similarity");

            migrationBuilder.AddColumn<double>(
                name: "market_1_canonical_similarity",
                table: "comparisons",
                type: "double precision",
                nullable: false,
                defaultValue: 0.0);
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "market_1_canonical_similarity",
                table: "comparisons");

            migrationBuilder.RenameColumn(
                name: "market_2_canonical_similarity",
                table: "comparisons",
                newName: "canonical_similarity");
        }
    }
}
