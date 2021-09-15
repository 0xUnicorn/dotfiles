source /home/unicorn/.config/nvim/vim-plug/plugins.vim

" NERDTree
nnoremap <silent> <C-n> :NERDTreeToggle<CR>
let NERDTreeShowHidden=1

" Spellcheck
set spelllang=en,da
nnoremap <silent> <F12> :set spell!<cr>
inoremap <silent> <F12> <C-O>:set spell!<cr>

"""""""""""""""""""
" Default configs "
"""""""""""""""""""

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

" Splits
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>
set splitbelow
set splitright

" Searches
set ignorecase " All searches will be case insensitive
set smartcase " All searches containing uppercase letter will be case sensitive

