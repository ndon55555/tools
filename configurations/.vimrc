" Specify plugin directory
call plug#begin('~/.vim/plugs')

" Git integration with Vim
Plug 'airblade/vim-gitgutter'

" vim-go
Plug 'fatih/vim-go', { 'do': ':GoUpdateBinaries' }

" Sidebar file navigation in vim
Plug 'scrooloose/nerdtree'

" Code completion in vim
Plug 'Shougo/deoplete.nvim'
Plug 'roxma/nvim-yarp'
Plug 'roxma/vim-hug-neovim-rpc'

" Completion framework and language server client
Plug 'neoclide/coc.nvim', { 'branch': 'release' }

" Initialize plugin system
call plug#end()



" NOTE: Comments in Vim are denoted with a double quote.
set background=dark
set number " Show line numbers
set hlsearch " Highlight search
:highlight lineNr ctermfg=white " Make line numbers white
set autoindent

" Tab size = 4
set tabstop=4
set shiftwidth=4
set expandtab

set updatetime=100

" Make backspace more intuitive
set backspace=indent,eol,start

" Enable mouse clicking
set mouse=a

" Invoke goimports on save
let g:go_fmt_command="goimports"

" Show hidden files in NERDTRee
let NERDTreeShowHidden=1

" Deoplete config
let g:deoplete#enable_at_startup=1
