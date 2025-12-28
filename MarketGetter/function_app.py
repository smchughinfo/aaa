import azure.functions as func
import logging
import Main

app = func.FunctionApp()

@app.timer_trigger(schedule="0 */15 * * * *", arg_name="myTimer", run_on_startup=False)
def market_processor(myTimer: func.TimerRequest) -> None:
    """
    Timer trigger that runs every 15 minutes.
    Schedule format: seconds minutes hours days months day-of-week
    "0 */15 * * * *" = every 15 minutes
    """
    logging.info('Market processor timer trigger function started.')

    try:
        Main.run_once()
        logging.info('Market processor completed successfully.')
    except Exception as e:
        logging.error(f'Market processor failed: {str(e)}')
        raise
