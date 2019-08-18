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

" Specify plugin directory
call plug#begin('~/.vim/plugs')

" Git integration with Vim
Plug 'airblade/vim-gitgutter'

" vim-go
Plug 'fatih/vim-go', { 'do': 'GoUpdateBinaries' }

" Sidebar file navigation
Plug 'scrooloose/nerdtree'

" Initialize plugin system
call plug#end()
