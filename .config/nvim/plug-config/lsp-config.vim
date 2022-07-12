" LSP mappings
nnoremap <silent> gd <cmd>lua vim.lsp.buf.definition()<CR>
nnoremap <silent> gD <cmd>lua vim.lsp.buf.declaration()<CR>
nnoremap <silent> gr <cmd>lua vim.lsp.buf.references()<CR>
nnoremap <silent> gi <cmd>lua vim.lsp.buf.implementation()<CR>
nnoremap <silent> gR <cmd>lua vim.lsp.buf.rename()<CR>
nnoremap <silent> K <cmd>lua vim.lsp.buf.hover()<CR>
nnoremap <silent> gk <cmd>lua vim.lsp.buf.signature_help()<CR>
nnoremap <silent> gp <cmd>lua vim.lsp.diagnostic.goto_prev()<CR>
nnoremap <silent> gn <cmd>lua vim.lsp.diagnostic.goto_next()<CR>
