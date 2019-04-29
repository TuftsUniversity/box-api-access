#!/bin/bash
export PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
log_dir=/usr/local/htdocs/archivesspace/logs
log_file=${log_dir}\/archivesspace.out
today_date=$( date '+%F' )
new_log_file=$( echo $log_file | sed "s/.out/-${today_date}.out"/)
new_log_file_gz=${new_log_file}\.gz
#service archivesspace stop
mv $log_file $new_log_file
gzip $new_log_file
# run the python script to upload $new_log_file_gz
python3 sendASpaceLogs.py $new_log_file_gz
rm $new_log_file_gz
#service archivesspace start
