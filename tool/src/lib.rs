//! `iwork-probe`: inspect the files Apple Pages writes, for clean-room format experiments.
//!
//! Everything here comes from public specifications (ZIP and the Protocol Buffers wire format).
//! Knowledge of Pages' own structures is added only once experiments in this repository have
//! established it.

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
pub mod package;
pub mod proto;
