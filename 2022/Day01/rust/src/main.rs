use std::fs;

fn main() {
    part_a();
    part_b()
}

fn part_a() {
    let cals = fs::read_to_string("/home/spy/dev/AoC2022/Day1/testinput.txt")
        .expect("Unable to read file");
    let res = cals
        .split("\n\n")
        .map(|elf| {
            elf.split("\n")
                .map(|num| num.parse::<u32>().unwrap())
                .sum::<u32>()
        })
        .max()
        .unwrap();

    println!("Elf with the max cals is carrying: {} calories", res)
}

fn part_b() {
    let cals = fs::read_to_string("/home/spy/dev/AoC2022/Day1/testinput.txt")
        .expect("Unable to read file");
    let mut res = cals
        .split("\n\n")
        .map(|elf| {
            elf.split("\n")
                .map(|num| num.parse::<u32>().unwrap())
                .sum::<u32>()
        })
        .collect::<Vec<_>>();
    res.sort_by(|a, b| b.cmp(a));

    println!(
        "The sum of the top 3 elves is: {} calories",
        res.iter().take(3).sum::<u32>().to_string()
    )
}
