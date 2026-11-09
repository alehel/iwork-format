//! `iwork-probe`: inspect the files Apple Pages writes, for clean-room format experiments.
//!
//! The decoders come from public specifications: ZIP, Snappy and the Protocol Buffers wire format.
//! Knowledge of Pages' own structures is added only once experiments in this repository have
//! established it, and each module that holds some names the experiment it comes from.

#![forbid(unsafe_code)]
#![deny(
    clippy::unwrap_used,
    clippy::expect_used,
    clippy::panic,
    clippy::unimplemented,
    clippy::todo,
    clippy::unreachable
)]

pub mod hex;
pub mod iwa;
pub mod package;
pub mod proto;
pub mod snappy;
pub mod text;
