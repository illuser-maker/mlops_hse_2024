from clearml import Task, InputModel

task = Task.init("For tests", "test_2")
logger = task.get_logger()

model = InputModel("35cb978764be41f4987584ac841ace6d")
model.connect(task)

logger.report_scalar("graph A", "series A", iteration=0, value=1)
logger.report_scalar("graph A", "series A", iteration=1, value=10)

task.upload_artifact("local file", "data/test_art")
task.close()