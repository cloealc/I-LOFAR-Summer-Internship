#! /bin/bash

# Cloe Alcaria
# June 2022
#
# This is a simple search script to dedisperse an input filterbank
# file, get a timeseries file, then a .prd file.
# It creates a range of DM values to investigate, and using
# hunt, the script searches this file for periodicities.

filfile=$1
stem=`stem $filfile`
echo $stem

# DM range definition

echo “Please enter lower DM boundary”
read lower
echo “Please enter upper DM boundary”
read upper
echo “Please enter DM steps”
read steps

# DM Loop

for dm in $(seq $lower $steps $upper )
do
      echo "DM is $dm"
      dedisperse $filfile".fil" -d $dm -i badchans > $filfile".tim"
      echo "dedisperse is done"
      seek $filfile".tim" -pulse -A
      echo "seek is done"
      step $lower $upper $steps > dmlist
      echo "dmlist updated"
      hunt $filfile
      echo "hunt is done"
      best $filfile".prd" -v
done

exit
