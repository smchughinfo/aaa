using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Data.Migrations
{
    /// <inheritdoc />
    public partial class AddEventForeignKey : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "embedding",
                table: "markets");

            migrationBuilder.CreateTable(
                name: "Event",
                columns: table => new
                {
                    id = table.Column<string>(type: "text", nullable: false),
                    embedding = table.Column<float[]>(type: "real[]", nullable: false),
                    question = table.Column<string>(type: "text", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Event", x => x.id);
                });

            migrationBuilder.CreateIndex(
                name: "IX_markets_event_id",
                table: "markets",
                column: "event_id");

            migrationBuilder.AddForeignKey(
                name: "FK_markets_Event_event_id",
                table: "markets",
                column: "event_id",
                principalTable: "Event",
                principalColumn: "id",
                onDelete: ReferentialAction.Cascade);
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_markets_Event_event_id",
                table: "markets");

            migrationBuilder.DropTable(
                name: "Event");

            migrationBuilder.DropIndex(
                name: "IX_markets_event_id",
                table: "markets");

            migrationBuilder.AddColumn<float[]>(
                name: "embedding",
                table: "markets",
                type: "real[]",
                nullable: false,
                defaultValue: new float[0]);
        }
    }
}
