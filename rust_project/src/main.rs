// fn main() {
//     println!("Hello, world!");
// }

use csv::Reader;
use anyhow::Result;
use std::collections::HashMap;

pub fn read_resume(file_path: &str) -> Result<HashMap<String, Vec<String>>> {
    let mut resume_data: HashMap<String, Vec<String>> = HashMap::new();
    let file = std::fs::File::open(file_path)?;
    let mut reader = Reader::from_reader(file);
    let headers = reader.headers()?.clone();
    for header in &headers {
        resume_data.insert(header.to_string(), Vec::new());
    }
    for record in reader.records() {
        let record = record?;
        for (i, value) in record.iter().enumerate() {
            let header = headers[i].to_string();
            resume_data.get_mut(&header).unwrap().push(value.to_string());
        }
    }
    Ok(resume_data)
}

pub fn check_variable(resume: &HashMap<String, Vec<String>>) {
    let variable_list = [
        "employment_holes",
        "volunteer",
        "worked_during_school",
        "special_skills",
    ];
    for variable in variable_list.iter() {
        if let Some(values) = resume.get(*variable) {
            let mut value_counts: HashMap<String, u32> = HashMap::new();
            for value in values {
                *value_counts.entry(value.to_string()).or_insert(0) += 1;
            }
            println!("{:?}", value_counts);
            println!("=======================");
        }
    }
}

fn main() -> Result<()> {
    let file_path = "resume.csv";
    let resume = read_resume(file_path)?;
    check_variable(&resume);
    Ok(())
}

