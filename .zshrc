# Use powerline
USE_POWERLINE="true"
# Source manjaro-zsh-configuration
if [[ -e /usr/share/zsh/manjaro-zsh-config ]]; then
  source /usr/share/zsh/manjaro-zsh-config
fi
# Use manjaro zsh prompt
if [[ -e /usr/share/zsh/manjaro-zsh-prompt ]]; then
  source /usr/share/zsh/manjaro-zsh-prompt
fi

# CUSTOM ALIASES

alias bw='bw --pretty'
alias vim='nvim'
alias l='ls -lh'
alias a='ls -lha'
alias ..='../'
alias ...='../../'
alias config='/usr/bin/git --git-dir=$HOME/.cfg --work-tree=$HOME'
