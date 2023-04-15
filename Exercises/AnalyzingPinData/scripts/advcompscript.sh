L1c=$1 
L1a=$2
L1b=$3

L2c=$4
L2a=$5  
L2b=$6

TLBe=$7
TLBa=$8
TLBp=$9

command=${10}

L2prf=${11}


if [ "$command" = "blackscholes" ];
then
    prompt="~/Downloads/parsec-3.0/parsec_workspace/executables/blackscholes 1 ~/Downloads/parsec-3.0/parsec_workspace/inputs/in_64K.txt prices.txt"
elif [ "$command" = "bodytrack" ];
then
    prompt="~/Downloads/parsec-3.0/parsec_workspace/executables/bodytrack ~/Downloads/parsec-3.0/parsec_workspace/inputs/sequenceB_4 4 4 4000 5 0 1"
elif [ "$command" = "canneal" ];
then
    prompt="~/Downloads/parsec-3.0/parsec_workspace/executables/canneal 1 15000 2000 ~/Downloads/parsec-3.0/parsec_workspace/inputs/400000.nets 128"
elif [ "$command" = "fluidanimate" ];
then
    prompt="~/Downloads/parsec-3.0/parsec_workspace/executables/fluidanimate 1 5 ~/Downloads/parsec-3.0/parsec_workspace/inputs/in_300K.fluid out.fluid"
elif [ "$command" = "freqmine" ];
then
    prompt="~/Downloads/parsec-3.0/parsec_workspace/executables/freqmine ~/Downloads/parsec-3.0/parsec_workspace/inputs/kosarak_990k.dat 790"
elif [ "$command" = "raytrace" ];
then
    prompt="~/Downloads/parsec-3.0/parsec_workspace/executables/rtview ~/Downloads/parsec-3.0/parsec_workspace/inputs/happy_buddha.obj -automove -nthreads 1 -frames 3 -res 1920 1080"
elif [ "$command" = "swaptions" ];
then
    prompt="~/Downloads/parsec-3.0/parsec_workspace/executables/swaptions -ns 64 -sm 40000 -nt 1"
elif [ "$command" = "streamcluster" ];
then
    prompt="~/Downloads/parsec-3.0/parsec_workspace/executables/streamcluster 10 20 128 16384 16384 1000 none output.txt 1"
else 
    echo "Wrong Prompt";
    exit;
fi

echo $prompt

eval pin -t ~/Downloads/parsec-3.0/advcomparch-ex1-helpcode/pintool/obj-intel64/simulator.so -o my_output.out "-L1c" "$L1c" -L1a "$L1a" -L1b "$L1b" -L2c "$L2c" -L2a "$L2a" -L2b "$L2b" -TLBe "$TLBe" -TLBa "$TLBa" -TLBp "$TLBp" -- "$prompt";

echo "L1: size=$L1c, associativity=$L1a, block=$L1b" >> text.txt;
echo "L2: size=$L2c, associativity=$L2a, block=$L2b" >> text.txt;
echo "TLB: size=$TLBe, associativity=$TLBa, page=$TLBp" >> text.txt;

echo -n "$command," >> text.txt && cat my_output.out | grep "IPC" | xargs -I {} echo {}"," >> text.txt;

echo " " >> text.txt;
echo " " >> text.txt;

rm my_output.out prices.txt;
