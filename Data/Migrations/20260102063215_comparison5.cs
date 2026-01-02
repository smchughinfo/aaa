using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Data.Migrations
{
    /// <inheritdoc />
    public partial class comparison5 : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropPrimaryKey(
                name: "PK_comparisons",
                table: "comparisons");

            migrationBuilder.DropColumn(
                name: "id",
                table: "comparisons");

            migrationBuilder.RenameColumn(
                name: "comporable",
                table: "comparisons",
                newName: "comparable");

            migrationBuilder.AlterColumn<string>(
                name: "market_2_id",
                table: "comparisons",
                type: "text",
                nullable: false,
                defaultValue: "",
                oldClrType: typeof(string),
                oldType: "text",
                oldNullable: true);

            migrationBuilder.AlterColumn<string>(
                name: "market_1_id",
                table: "comparisons",
                type: "text",
                nullable: false,
                defaultValue: "",
                oldClrType: typeof(string),
                oldType: "text",
                oldNullable: true);

            migrationBuilder.AlterColumn<bool>(
                name: "comparable",
                table: "comparisons",
                type: "boolean",
                nullable: true,
                oldClrType: typeof(bool),
                oldType: "boolean");

            migrationBuilder.AddPrimaryKey(
                name: "PK_comparisons",
                table: "comparisons",
                columns: new[] { "market_1_id", "market_2_id" });

            migrationBuilder.CreateIndex(
                name: "IX_comparisons_market_2_id",
                table: "comparisons",
                column: "market_2_id");

            migrationBuilder.AddForeignKey(
                name: "FK_comparisons_markets_market_1_id",
                table: "comparisons",
                column: "market_1_id",
                principalTable: "markets",
                principalColumn: "id",
                onDelete: ReferentialAction.Cascade);

            migrationBuilder.AddForeignKey(
                name: "FK_comparisons_markets_market_2_id",
                table: "comparisons",
                column: "market_2_id",
                principalTable: "markets",
                principalColumn: "id",
                onDelete: ReferentialAction.Cascade);
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_comparisons_markets_market_1_id",
                table: "comparisons");

            migrationBuilder.DropForeignKey(
                name: "FK_comparisons_markets_market_2_id",
                table: "comparisons");

            migrationBuilder.DropPrimaryKey(
                name: "PK_comparisons",
                table: "comparisons");

            migrationBuilder.DropIndex(
                name: "IX_comparisons_market_2_id",
                table: "comparisons");

            migrationBuilder.RenameColumn(
                name: "comparable",
                table: "comparisons",
                newName: "comporable");

            migrationBuilder.AlterColumn<string>(
                name: "market_2_id",
                table: "comparisons",
                type: "text",
                nullable: true,
                oldClrType: typeof(string),
                oldType: "text");

            migrationBuilder.AlterColumn<string>(
                name: "market_1_id",
                table: "comparisons",
                type: "text",
                nullable: true,
                oldClrType: typeof(string),
                oldType: "text");

            migrationBuilder.AlterColumn<bool>(
                name: "comporable",
                table: "comparisons",
                type: "boolean",
                nullable: false,
                defaultValue: false,
                oldClrType: typeof(bool),
                oldType: "boolean",
                oldNullable: true);

            migrationBuilder.AddColumn<string>(
                name: "id",
                table: "comparisons",
                type: "text",
                nullable: false,
                defaultValue: "");

            migrationBuilder.AddPrimaryKey(
                name: "PK_comparisons",
                table: "comparisons",
                column: "id");
        }
    }
}
