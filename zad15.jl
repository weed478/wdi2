# TODO stop checking if prime

module Main

using Primes

# ndigits - base(ndigits+1) encoding (maximum number of digits)
# len - actual number of digits

function getdigitmap(n::Int128, ndigits::Int128)::Int128
    digitmap::Int128 = 0
    for d::Int128 in digits(n)
        digitmap += (ndigits + Int128(1))^d
    end
    digitmap
end

function getsump(digitmap::Int128, ndigits::Int128, len::Int128)::Int128
    digitmap ÷= ndigits + Int128(1) # remove 0s count
    Σ::Int128 = 0
    for d::Int128 in Int128(1):Int128(9)
        digitmap::Int128, dcount::Int128 = divrem(digitmap, ndigits + Int128(1))
        Σ += dcount * d ^ len
    end
    Σ
end

function testsump(digitmap::Int128, ndigits::Int128, len::Int128)
    sump::Int128 = getsump(digitmap, ndigits, len)
    if Primes.isprime(sump)
        if getdigitmap(sump, ndigits) == digitmap
            println(sump)
        end
    end
end

function forallcombos(ndigits::Int128, depth::Int128 = Int128(10), digitmap::Int128 = Int128(0), clen::Int128 = Int128(0))
    if depth == Int128(0)
        testsump(digitmap, ndigits, clen)
    else
        Threads.@threads for i::Int128 in Int128(0):ndigits - clen
            forallcombos(ndigits, depth - Int128(1), digitmap * (ndigits+Int128(1)) + i, clen + i)
        end
    end
end

# 2
# 3
# 5
# 35452590104031691935943
# 7
# 449177399146038697307
# 28116440335967
# 19.79s

function main()
    forallcombos(Int128(23))
end

end
