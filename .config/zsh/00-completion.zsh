# Completion system
fpath=(~/.config/zsh/completions $fpath)
autoload -Uz compinit
compinit

# Descriptions and colors
zstyle ':completion:*:descriptions' format '[%d]'
zstyle ':completion:*:messages' format '%F{yellow}%d%f'
zstyle ':completion:*:warnings' format '%F{red}No matches for:%f %d'
zstyle ':fzf-tab:*' fzf-flags --height=40% --layout=reverse --border
zstyle ':completion:*' list-colors ${(s.:.)LS_COLORS}
