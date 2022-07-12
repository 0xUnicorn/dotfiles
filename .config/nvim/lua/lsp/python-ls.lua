local util = require("lspconfig/util")

require'lspconfig'.pyright.setup{
    capabilities = capabilities,
    root_dir = function(fname)
    return util.root_pattern(".git", "setup.py",  "setup.cfg", "pyproject.toml", "requirements.txt")(fname) or
      util.path.dirname(fname)
  end
}

