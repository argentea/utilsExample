#!/bin/zsh
#

add_window(){
	tmux new-window -t $1 -n $2 -d $3
}


createMonitorTmux(){
	SESSIONNAME="monitor"
	add_window $SESSIONNAME "local" "htop"
	tmux select-window -t 1
	tmux split-window -v -d watch -n 3 iostat /dev/nvme0n1
}

lb(){

	if [[ $# == 0 ]]; then
		SESSIONNAME="tmp"
	else
		SESSIONNAME=$1
	fi

	tmux has-session -t $SESSIONNAME 2&> /dev/null;

	if [[ $? != 0 ]]; then
		tmux new-session -s $SESSIONNAME -d
		if [[ $SESSIONNAME = "monitor" ]]; then
			createMonitorTmux
		fi
	fi


	tmux attach -t $SESSIONNAME
}
