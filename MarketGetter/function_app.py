import azure.functions as func
import logging

app = func.FunctionApp()

@app.timer_trigger(schedule="0 */15 * * * *", arg_name="myTimer", run_on_startup=True)
def get_markets(myTimer: func.TimerRequest) -> None:
    """
    Timer trigger that runs every 15 minutes.
    Schedule format: seconds minutes hours days months day-of-week
    "0 */15 * * * *" = every 15 minutes
    """
    logging.info('Market processor timer trigger function started.')

    try:
        import main
        main.run_once()
        logging.info('Market processor completed successfully.')
    except Exception as e:
        logging.error(f'Market processor failed: {str(e)}')
        raise
