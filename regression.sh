#!/bin/bash

for easm in tests/*.easm; do
    alf="$(echo "${easm}" | sed 's/easm/alf/g')"
    out="$(echo "${easm}" | sed 's/easm/out/g')"
    output=$(python asm.py --asm-file "${easm}")
    echo "${output}" > "${out}"

    diff -w -q "${alf}" "${out}"
    res="$?"
    if [[ $res -eq 0 ]] ; then
        echo "${easm} OK"
    else
        echo "${easm} NOK"
    fi
done