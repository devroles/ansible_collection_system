if !exists("b:loaded_python_ftplugin_opts")
	let b:loaded_python_ftplugin_opts=1

	setlocal tabstop=4
	setlocal shiftwidth=4
	setlocal expandtab
	setlocal softtabstop=4
	" flake8 settings
	if filereadable("/usr/bin/python3-flake8")
		let g:flake8_cmd="/usr/bin/python3-flake8"
	else
		let g:flake8_cmd="/usr/bin/flake8"
	endif
	" show 80 column boundary in insert mode only
	" https://stackoverflow.com/questions/11774904/vim-scripting-if-vim-version-is-7-3
	if version > 702
		augroup ColorcolumnOnlyInInsertMode
			autocmd!
			autocmd InsertEnter * setlocal colorcolumn=80
			autocmd InsertLeave * setlocal colorcolumn=0
		augroup END
	endif
endif
