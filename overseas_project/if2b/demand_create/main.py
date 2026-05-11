
from locust import LoadTestShape, HttpUser
import math

from overseas_project.if2b.demand_create.customer_service import *


class StepShape(LoadTestShape):
    """
        step_time -- 步骤之间的时间
        step_load -- 用户在每一步增加数量
        spawn_rate -- 用户在每一步式每秒停止/启动数量
        time_limit -- 时间限制，以秒为单位
    """
    step_time = 600
    step_load = 1
    spawn_rate = 1
    time_limit = 7200

    def tick(self):
        run_time = self.get_run_time()

        if run_time > self.time_limit:
            return None

        current_step = math.floor(run_time / self.step_time) + 1
        return (current_step * self.step_load, self.spawn_rate)


class myClass(HttpUser):

    host = 'https://if2b-alpha.casstime.com'

    def on_start(self):
        self.client.headers = {'Content-type': 'application/json'}

    tasks = {
        demand_create: 1
    }

    min_wait = 100
    max_wait = 100


if __name__ == '__main__':
    filename = __file__
    master_cmd = 'start locust -f ' + filename + ' --master --web-host=0.0.0.0'
    worker_cmd = ' && start locust -f ' + filename + ' --worker'
    total_cmd = master_cmd + worker_cmd * 7
    os.system(total_cmd)






