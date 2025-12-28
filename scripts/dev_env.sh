#!/usr/bin/env bash

SESSION_NAME="MJBPythonLibrary"

if tmux has-session -t "${SESSION_NAME}" 2>/dev/null; then
    echo "Session ${SESSION_NAME} already exist"
    tmux attach -t "${SESSION_NAME}"
else 
    echo "Session ${SESSION_NAME} does not exist"
    tmux new-session -d -s "${SESSION_NAME}"
    tmux new-window -t "nvim"
    tmux new-window -t "claude"
    tmux new-window -t "lazygit"
fi

echo "Martin Bullman"
