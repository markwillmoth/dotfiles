# Prompt setup
autoload -Uz promptinit; promptinit

# Nerd font symbols
PROMPT='%F{cyan}%f %F{green}%n%f@%F{blue}%m%f:%F{yellow}%~%f
%F{cyan}→%f '

# Git info in right prompt
autoload -Uz vcs_info
precmd() { vcs_info }
zstyle ':vcs_info:*' enable git
RPROMPT='%F{magenta}${vcs_info_msg_0_}%f'

[[ -f ~/.p10k.zsh ]] && source ~/.p10k.zsh

