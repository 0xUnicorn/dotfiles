source /home/unicorn/.config/nvim/vim-plug/plugins.vim

" LSPConfig
source ~/.config/nvim/plug-config/lsp-config.vim
luafile ~/.config/nvim/lua/lsp/python-ls.lua

" Autocomplete (nvim-cmp)
luafile ~/.config/nvim/lua/plugins/cmp-config.lua

" Auto Pairs
let g:AutoPairsShortcutFastWrap = '<C-e>'

" NERDTree
nnoremap <silent> <C-n> :NERDTreeToggle<CR>
let NERDTreeShowHidden=1

" Spellcheck
set spelllang=en,da
nnoremap <silent> <F12> :set spell!<cr>
inoremap <silent> <F12> <C-O>:set spell!<cr>

" Polyglot syntaxes
let g:python_highlight_all = 1

" VirtualEnv
let g:virtualenv_directory = $PWD
let g:virtualenv_name = '.venv'

" VIM Airline
let g:airline_theme='dark'
let g:airline_powerline_fonts = 1
let g:airline#extensions#virtualenv#enabled = 1
let g:airline#extensions#branch#enabled = 1
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#fnamemod = ':t'
let g:airline#parts#ffenc#skip_expected_string='utf-8[unix]'

if !exists('g:airline_symbols')
    let g:airline_symbols = {}
endif

" unicode symbols
let g:airline_left_sep = '»'
let g:airline_left_sep = '▶'
let g:airline_right_sep = '«'
let g:airline_right_sep = '◀'
let g:airline_symbols.linenr = '␊'
let g:airline_symbols.linenr = '␤'
let g:airline_symbols.linenr = '¶'
let g:airline_symbols.branch = '⎇'
let g:airline_symbols.paste = 'ρ'
let g:airline_symbols.paste = 'Þ'
let g:airline_symbols.paste = '∥'
let g:airline_symbols.whitespace = 'Ξ'

" airline symbols
let g:airline_left_sep = ''
let g:airline_left_alt_sep = ''
let g:airline_right_sep = ''
let g:airline_right_alt_sep = ''
let g:airline_symbols.branch = ''
let g:airline_symbols.readonly = ''
let g:airline_symbols.linenr = ''


"""""""""""""""""""
" Default configs "
"""""""""""""""""""

" Mapping leader
:let mapleader = "-"
" Leader save
nnoremap <Leader><space> :w<CR>
" Leader run python unittests
nnoremap <Leader>u :!python3 -m unittest discover<CR>
nnoremap <Leader>p :!python3 -m pytest <CR>
nnoremap <Leader>P :!python3 -m pytest -n 6<CR>

" Color settings
colorscheme dracula
set termguicolors
let &t_8f = "\<Esc>[38;2;%lu;%lu;%lum"
let &t_8b = "\<Esc>[48;2;%lu;%lu;%lum"

" Colorizer
lua require'colorizer'.setup()

" Line numbers
set number relativenumber

" Show Tabs, Trailingspaces
set list
set listchars=tab:>\ ,trail:•,nbsp:␣
set encoding=utf-8

" Spaces & Tabs
set tabstop=4       " number of visual spaces per TAB
set softtabstop=4   " number of spaces in tab when editing
set shiftwidth=4    " number of spaces to use for autoindent
set expandtab       " tabs are space
set autoindent
set copyindent      " copy indent from the previous line

" Python PEP8 indentation
au BufNewFile,BufRead *.py
    \ setlocal textwidth=79
    \| setlocal fileformat=unix

" Python configurations
let g:python3_host_prog = '/usr/bin/python3'

" Full stack development
au BufNewFile,BufRead *.js, *.html, *.css
    \ setlocal tabstop=2
    \| setlocal softtabstop=2
    \| setlocal shiftwidth=2

" Splits
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>
set splitbelow
set splitright

" Move between buffers
noremap . :bn<CR>
noremap , :bp<CR>
noremap <Leader>- :bdelete<CR>

" Searches
set ignorecase " All searches will be case insensitive
set smartcase " All searches containing uppercase letter will be case sensitive
