# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="/home/kunpeng/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="bira"

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in ~/.oh-my-zsh/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to automatically update without prompting.
# DISABLE_UPDATE_PROMPT="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS=true

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in ~/.oh-my-zsh/plugins/*
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git extract z)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
alias lps='lp -o sides=two-sided-short-edge'
alias lpl='lp -o sides=two-sided-long-edge'
alias zs='zathura'
alias c='clear'
alias p='cd -'
alias b='cd ..'
alias cdl='cd ~/data/learn'
alias cdd='cd ~/Downloads'
alias cde='cd ~/data/eikonalEquation'
alias cdr='cd ~/data/research'
alias cdf='cd ~/data/justForFun'
alias cdb='cd ~/data/book'
alias cda='cd ~/data/acbb'
alias cdp='cd ~/data/paper'
alias cdg='cd ~/data/git'
alias tmux='tmux -u'
alias mplay='amarok'
alias utar='tar -zxvf'
alias chrome='google-chrome'
alias xc='xclip'
alias evi='evince'
alias ff='firefox'
alias ssh='ssh -X'
alias cbbpy='vim "$(date +"%Y_%m_%d_%H_%M").py'
alias trb='tree -hf -I build'

#alias findhcpp="find ./ -name build -prune -o -type f -name '*.h' -print -o -type f -name '*.cpp' -print"
export myLogFile=~/log/mylog



mkvRename() {
	autoload -U regexp-replace
	if [[ $# == 0 ]]; then
		echo "mkvRename [DIRECTORY] [SUFFIX1] [SUFFIX2]"
		echo "SUFFIX1: the name you want to change to"
		echo "SUFFIX2: the file you want to change"
		return
	fi
	if [[ $1 == "-h" ]]; then
		echo "mkvRename [DIRECTORY] [SUFFIX1] [SUFFIX2]"
		echo "SUFFIX1: the name you want to change to"
		echo "SUFFIX2: the file you want to change"
		return
	fi
	if [[ $# == 3 ]]; then
		sourcesuffix=$2;
		aimsuffix=$3;
	else
		sourcesuffix="mkv";
		aimsuffix="srt";
	fi
	echo "use the name of $sourcesuffix to rename $aimsuffix"
	raw_array=($1/*)
	source_array=()
	toChange_array=()
	echo "rename for subtitle"

	for i in "${(@k)raw_array}"; do
		if [[ $i =~ "\.${sourcesuffix}\b" ]]; then
			tmp="$i";
			regexp-replace tmp '\.\w+$' ''
			source_array+=($tmp);
		fi
		if [[ $i =~ "\.${aimsuffix}\b" ]]; then
			tmp="$i";
			toChange_array+=($tmp);
		fi
	done

	for (( i = 0; i < ${#toChange_array[@]}; i++ )); do
		mv ${toChange_array[@]:$i:1} "${source_array[@]:$i:1}.${aimsuffix}";
		echo "mv ${toChange_array[@]:$i:1} to ${source_array[@]:$i:1}.${aimsuffix} for ${source_array[@]:$i:1}.${sourcesuffix}"
	done
}

mmd() {
	if [[ $# == 0 ]]; then
		echo "open a new log md"
		mdFileNum="$(ls -1q ~/log/*.md|wc -l)"
		newFileName=~/log/log${mdFileNum}.md
		touch "${newFileName}"
		typora "${newFileName}" &
		return
	fi
	if [[ $# == 1 ]]; then
		mdFileNum="$(ls -1q ~/log/*.md|wc -l)"
		echo "open ${1}${mdFileNum}.md"
		newFileName=~/log/${1}${mdFileNum}.md
		touch "${newFileName}"
		typora "${newFileName}" &
		return
	fi
	echo "only 1 paramater needed"
	return
}

#find files which names matchs the argument
#only support find in ./
#omit directory build/ in default
#example: findf "*.h" "*.cu"
findf() {
	if [[ $# == 0 ]]; then
		find ./ -name build -prune -o -type f -name '*.h' -print -o -type f -name '*.cpp' -print
		return
	else
		findargs="./ -name build -prune ";
		for i; do
			findargs="${findargs}-o -type f -name $i -print "
		done
		find ${(z)findargs}
		unset findargs
	fi

}

ml() {
	if [[ $# == 0 ]]; then
		echo "You can use this to write log to ${myLogFile}, nl is newline"
	else
		if test -f "${myLogFile}"; then
			string="$(date +"%Y_%m_%d_%H_%M")";
			string="${string} :\n";
			for i; do
				if [[ $i == "nl" ]]; then
					string="${string}\n ";
				else
					string="${string}$i ";
				fi
			done
			echo ${string} >> ${myLogFile};
			echo "writen"
			unset string
		else
			touch "${myLogFile}"
			echo "create log file in ${myLogFile}"
		fi
	fi
}

fl() {
	if [[ $# == 0 ]]; then
		tail -n 10 ${myLogFile};
	else
		lineNum=$(($1*2))
		tail -n ${lineNum} ${myLogFile}
	fi
}

ggggg() {	
	echo $(date +"%Y_%m_%d_%H_%M");
}

#alias ohmyzsh="mate ~/.oh-my-zsh"
# Highlight the current autocomplete option
zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"

# Better SSH/Rsync/SCP Autocomplete
# Allow for autocomplete to be case insensitive

# Initialize the autocompletion
autoload -Uz compinit && compinit -i
h=()
if [[ -r ~/.ssh/config ]]; then
  h=($h ${${${(@M)${(f)"$(cat ~/.ssh/config)"}:#Host *}#Host }:#*[*?]*})
fi
#if [[ -r ~/.ssh/known_hosts ]]; then
#  h=($h ${${${(f)"$(cat ~/.ssh/known_hosts{,2} || true)"}%%\ *}%%,*}) 2>/dev/null
#fi
if [[ $#h -gt 0 ]]; then
  zstyle ':completion:*:(scp|ssh|rsync):*' hosts $h
  zstyle ':completion:*:slogin:*' hosts $h
fi
zstyle ':completion:*:ssh:argument-1:*' tag-order hosts
zstyle ':completion:*' completer _expand _complete _ignored _correct _approximate
zstyle ':completion:*' expand suffix
zstyle ':completion:*' file-sort access
zstyle ':completion:*' list-suffixes true
zstyle ':completion:*' matcher-list '+' '+m:{[:lower:]}={[:upper:]} m:{[:lower:][:upper:]}={[:upper:][:lower:]} r:|[._-]=* r:|=*' 'r:|[._-]=* r:|=* l:|=*'
zstyle ':completion:*' max-errors 1
zstyle ':completion:*' prompt 'c%e'
zstyle :compinstall filename '/home/kunpeng/.zshrc'
bu() {
	if [[ $# == 0 ]]; then
		echo "usage:\n\tbuild r(rebuild by remove build/)\n\tbuild c(continue build without cmake .. )\n\tbuild n(new build with cmake ..)";
		echo "\tbuild d(with debug)"
	fi
	CurrentFile=${PWD##*/};
	InBuildFile=0;
	runResult=0;
	if [[ ${CurrentFile} == "build" ]]; then
		InBuildFile=1;
		print InBuildFile
		cd ..;
	else
		InBuildFile=2;
	fi
	if [[ $1 == 'r' && $# == 1 ]]; then
		rm -r build;
		mkdir build;
		cd build;
		if cmake .. && make -j30; then
			echo "good news"
			runResult=0;
		else
			echo "bad news"
			runResult=1;
		fi
		cp ./compile_commands.json ..;
		if [[ InBuildFile == 2 ]]; then
			InBuildFile=3;
		fi
	fi
	if [[ $1 == 'c' && $# == 1 ]]; then
		cd build;
		if make -j30; then
			echo "good news"
			runResult=0;
		else
			echo "bad news"
			runResult=1;
		fi
		cp ./compile_commands.json ..;
		if [[ InBuildFile == 2 ]]; then
			InBuildFile=3;
		fi
	fi
	if [[ $1 == 'n' && $# == 1 ]]; then
		cd build;
		if cmake .. && make -j30; then
			echo "good news"
			runResult=0;
		else
			echo "bad news"
			runResult=1;
		fi
		cp ./compile_commands.json ..;
		if [[ InBuildFile == 2 ]]; then
			InBuildFile=3;
		fi

	fi
	if [[ $1 == 'd' && $# == 1 ]]; then
		cd build;
		if cmake -DCMAKE_BUILD_TYPE=Debug .. && make -j30; then
			echo "good news"
			runResult=0;
		else
			echo "bad news"
			runResult=1;
		fi
		cp ./compile_commands.json ..;
		if [[ InBuildFile == 2 ]]; then
			InBuildFile=3;
		fi
	fi

	if [[ InBuildFile == 3 ]]; then
		cd ..;
	fi
	return runResult
}



ZSH_TMUX_AUTOSTART=true
autoload -Uz compinit
compinit
# End of lines added by compinstall
# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
bindkey -v

#source /etc/profile.d/undistract-me.sh
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/kunpeng/anaconda3/bin/conda' 'shell.${aimsuffix}ash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/kunpeng/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/kunpeng/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/kunpeng/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

conda activate base

export PATH=/usr/local/cuda/bin:${PATH}
export LD_LIBRARY_PATH=/usr/loca/cuda/lib64:${LD_LIBRARY_PATH}

export PATH=/home/kunpeng/bin/gcc-10.2.0/bin${PATH:+:${PATH}}
export PATH=/usr/local/cuda-11.5/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/home/kunpeng/bin/gcc-10.2.0/lib64:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/usr/local/cuda-11.5/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
export CC=/home/kunpeng/bin/gcc-10.2.0/bin/gcc-10.2.0
export CXX=/home/kunpeng/bin/gcc-10.2.0/bin/g++-10.2.0
export FC=/home/kunpeng/bin/gcc-10.2.0/bin/gfortran-10.2.0

