#!/bin/bash
# this script from https://github.com/greymd/ssh_opt_parse
set -u

## Options work individually
readonly SSH_SINGLE_OPTS="[1246AaCfGgKkMNnqsTtVvXxYy]"
## Options require its argument(s).
readonly SSH_MULTI_OPTS="[bcDEeFIiJLlmOopQRSWw]"
readonly SSH_CONFIG_FILE=${SSH_CONFIG_FILE:-${HOME}/.ssh/config}

SSH_PORT=
SSH_USER=
SSH_HOST=
SSH_COMMAND=()

ssh_opt_show_result () {
  printf "SSH_PORT\\t%s\\n" "${SSH_PORT}"
  printf "SSH_USER\\t%s\\n" "${SSH_USER}"
  printf "SSH_HOST\\t%s\\n" "${SSH_HOST-}"
  printf "SSH_COMMAND\\t%s\\n" "${SSH_COMMAND[*]## }"
}

ssh_opt_parse_options () {
  while (( $# > 0 )) ;do
    case "$1" in
      --)
        break
        ;;

      -*)
        if [[ "$1" =~ -${SSH_SINGLE_OPTS}*p$ ]]; then
          SSH_PORT="$2"
          shift
          shift
        elif [[ "$1" =~ -${SSH_SINGLE_OPTS}*p. ]]; then
          SSH_PORT=$(sed "s/-${SSH_SINGLE_OPTS}*p//" <<<"$1")
          shift
        elif [[ "$1" =~ -${SSH_SINGLE_OPTS}*l$ ]] ;then
          SSH_USER="$2"
          shift
          shift
        elif [[ "$1" =~ -${SSH_SINGLE_OPTS}*l. ]] ;then
          SSH_USER=$(sed "s/-${SSH_SINGLE_OPTS}*l//" <<<"$1")
          shift
        elif [[ "$1" =~ -${SSH_SINGLE_OPTS}+$ ]] ;then
          shift
        elif [[ "$1" =~ -${SSH_SINGLE_OPTS}*${SSH_MULTI_OPTS}$ ]] ;then
          shift
          shift
        fi
        ;;

      *)
        if [[ -n "${SSH_HOST}" ]] ; then
          break
        fi
        if [[ -z "${SSH_HOST}" ]] && [[ "$1" =~ ^.*@.*$ ]] ; then
          SSH_USER="${1%%@*}"
        fi
        if [[ -z "${SSH_HOST}" ]] ;then
          SSH_HOST="${1##*@}"
        fi
        shift
        ;;
    esac
  done
  # Rest of arguments may be command line
  if (( $# > 0 )); then
    SSH_COMMAND=("$1")
    shift
  fi
  for _arg in "$@"; do
    SSH_COMMAND=("${SSH_COMMAND[@]-}" "$_arg")
  done

  if [[ -n "${SSH_HOST}" ]]; then
    if [[ -z "${SSH_USER}" ]] ;then
      SSH_USER=$(ssh_opt_get_value_from_config "${SSH_HOST}" "User")
      # If there is no record for the host in the ~/.ssh/config.
      if [[ $? -eq 1 ]]; then
        SSH_USER=$(whoami)
      fi
    fi

    if [[ -z "${SSH_PORT}" ]] ;then
      SSH_PORT=$(ssh_opt_get_value_from_config "${SSH_HOST}" "Port")
      # If there is no record for the host in the ~/.ssh/config.
      if [[ $? -eq 1 ]]; then
        SSH_PORT=22
      fi
    fi
  fi
}

ssh_opt_get_value_from_config () {
  local _host="$1"
  local _key="$2"
    perl -anpe 's/^\s+//' "${SSH_CONFIG_FILE}" \
    | grep -v '^#' \
    | perl -anle '$F[0] =~ /^(HOST|MATCH)$/i and $key=$F[1]; print "$key\t$_"' \
    | perl -sanle '$F[0] eq $host and $F[1] =~ /^$key$/i and print $F[2]' -- -host="${_host}" -key="${_key}" \
    | grep .
    return $?
}

ssh_opt_parse () {
  if ! [[ "$1" =~ ssh ]]; then
    return
  fi
  shift # remove beginning of "ssh"
  ssh_opt_parse_options "${1+"$@"}"
  ssh_opt_show_result
}

## -------------------------
## Entry point
## -------------------------
ssh_opt_parse "${1+"$@"}"