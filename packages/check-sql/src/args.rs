// Copyright (C) 2023 Checkmk GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
// conditions defined in the file COPYING, which is part of this source code package.

use crate::constants;
use clap::Parser;
use std::path::PathBuf;

#[derive(Parser, Default)]
#[command(about = "Check SQL plugin.", version = constants::VERSION)]
pub struct Args {
    /// Enable verbose output. Use once (-v) for logging level DEBUG and twice (-vv) for logging
    /// level TRACE.
    #[arg(short, long, action = clap::ArgAction::Count)]
    pub verbose: u8,

    /// Sends log to stderr.
    #[arg(short = 'l', long)]
    pub display_log: bool,
    /// Prints config, parameters, important variables
    #[arg(short, long)]
    pub show_config: bool,

    /// Use custom log dir
    #[arg(long)]
    pub log_dir: Option<PathBuf>,

    /// Use custom temp dir
    #[arg(long)]
    pub temp_dir: Option<PathBuf>,

    /// All sections are generated as sync
    #[arg(long)]
    pub disable_caching: bool,

    ///  
    #[arg(long)]
    pub clean_caches: bool,

    /// Use custom config file
    #[arg(short, long)]
    pub config_file: Option<PathBuf>,
}

impl Args {
    pub fn logging_level(&self) -> Option<log::Level> {
        match self.verbose {
            2.. => Some(log::Level::Trace),
            1 => Some(log::Level::Trace),
            _ => None,
        }
    }
}
