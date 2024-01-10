# 0x14-queuing_system_in_js

kill $(ps -e | grep redis-server | awk '{print $1}')

when a command line ends with the &, the shell does not wait for the command to finish. You will get your shell prompt back while the command executes in the background

https://www.tabnine.com/code/javascript/functions/redis/print

https://www.tutorialspoint.com/node-js-util-promisify-method

https://ifelse.io/2016/02/23/using-node-redis-and-kue-for-priority-job-processing/