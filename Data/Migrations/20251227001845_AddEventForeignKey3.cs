using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Data.Migrations
{
    /// <inheritdoc />
    public partial class AddEventForeignKey3 : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_markets_Event_event_id",
                table: "markets");

            migrationBuilder.DropPrimaryKey(
                name: "PK_Event",
                table: "Event");

            migrationBuilder.RenameTable(
                name: "Event",
                newName: "events");

            migrationBuilder.AddPrimaryKey(
                name: "PK_events",
                table: "events",
                column: "id");

            migrationBuilder.AddForeignKey(
                name: "FK_markets_events_event_id",
                table: "markets",
                column: "event_id",
                principalTable: "events",
                principalColumn: "id",
                onDelete: ReferentialAction.Cascade);
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_markets_events_event_id",
                table: "markets");

            migrationBuilder.DropPrimaryKey(
                name: "PK_events",
                table: "events");

            migrationBuilder.RenameTable(
                name: "events",
                newName: "Event");

            migrationBuilder.AddPrimaryKey(
                name: "PK_Event",
                table: "Event",
                column: "id");

            migrationBuilder.AddForeignKey(
                name: "FK_markets_Event_event_id",
                table: "markets",
                column: "event_id",
                principalTable: "Event",
                principalColumn: "id",
                onDelete: ReferentialAction.Cascade);
        }
    }
}
