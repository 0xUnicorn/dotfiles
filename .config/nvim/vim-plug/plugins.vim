" auto-install vim-plug
if empty(glob('~/.config/nvim/autoload/plug.vim'))
  silent !curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  "autocmd VimEnter * PlugInstall
  "autocmd VimEnter * PlugInstall | source $MYVIMRC
endif

call plug#begin('~/.config/nvim/autoload/plugged')

    " Better Syntax Support
    Plug 'sheerun/vim-polyglot'
    " File Explorer
    Plug 'preservim/nerdtree'
    " Markdown Preview
    Plug 'iamcco/markdown-preview.nvim', { 'do': { -> mkdp#util#install() }, 'for': ['markdown', 'vim-plug']}
    " VIM/TMUX Navigator
    "" Plug 'christoomey/vim-tmux-navigator'
    " Indent Python correctly to PEP8
    Plug 'Vimjas/vim-python-pep8-indent'
    " Colorizer
    Plug 'norcalli/nvim-colorizer.lua'
    " Dracula theme
    Plug 'dracula/vim',{'as':'dracula'}
    " DevIcons
    Plug 'ryanoasis/vim-devicons'
    " VIM Airline bar + themes
    Plug 'vim-airline/vim-airline'
    Plug 'vim-airline/vim-airline-themes'
    " GIT Support
    Plug 'tpope/vim-fugitive'
    " Auto Pairs
    Plug 'jiangmiao/auto-pairs'
    " Virtual-env support
    Plug 'jmcantrell/vim-virtualenv'
    " NVIM LSP Config
    Plug 'neovim/nvim-lspconfig'
    " LSP Saga
    "" Plug 'glepnir/lspsaga.nvim'
    " VIM vsnip
    Plug 'hrsh7th/vim-vsnip'
    " NVIM Completion engine
    Plug 'hrsh7th/nvim-cmp'
    " NVIM-CMP sources
    Plug 'hrsh7th/cmp-nvim-lsp'
    Plug 'hrsh7th/cmp-buffer'
    Plug 'hrsh7th/cmp-path'

call plug#end()
