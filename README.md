<!--
Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.
SPDX-License-Identifier: BSD-3-Clause
-->
# Package branch — CentOS 10 Stream (`c10s`)

**This is the branch you work on.** It holds the `mink-optee-client.spec` RPM's spec file and
`sources` pointer, plus the CI workflows that build and publish them.

## mink-optee-client RPM package

This RPM packages [`OPTEE/optee_client`](https://github.com/OP-TEE/optee_client) with mink based changes
—  This package provides a Qualcomm-adapted build of the upstream OP-TEE PKCS#11
TEE client library (libckqteec), designed to communicate with the Qualcomm
Trusted Execution Environment (QTEE) via the MinkIPC transport layer.
It is based on the upstream OP-TEE Client source (https://github.com/OP-TEE/optee_client)
at version 4.0.0, with minimal patches applied to link against the Qualcomm
MinkIPC stack (libminkteec, libminkadaptor) instead of the standard OP-TEE transport.

## Package contents

| File | Purpose |
|---|---|
| [`mink-optee-client.spec`](mink-optee-client.spec) | RPM spec for `mink-optee-client.spec`. Builds via autotools (`cmake` + `%cmake_build`), installs the `libckqteec` library  generated inline in `%install`. |
| [`sources`](sources) | dist-git checksum pointer for the upstream `v4.0.0` release tarball (SHA512). The tarball itself is never committed — see [`docs/workflows.md`](docs/workflows.md) for the lookaside-cache model. |
| [`.github/workflows/`](.github/workflows) | build-on-pr.yml, pkg-release.yml CI workflow files. |

## Getting started

### Update the version

Two edits, every time:

1. Bump `Version:` in [`mink-optee-client.spec`](mink-optee-client.spec) (and the
   `Source0:` URL if the upstream release layout changed).
2. Recompute the checksum:
   ```bash
   sha512sum --tag mink-optee-client-<newversion>.tar.gz > sources
   ```

Commit both, open a PR against this branch, merge, then run **Release**. The
first release fetches the new upstream tarball, verifies it, and caches it back
automatically.

### Open a PR

`build-on-pr` fetches the tarball (from the lookaside cache, or from the spec's
`Source` URL on a cache miss), verifies the checksum, and builds the RPM.
Download it from the run's **Artifacts**.

### Release

**Actions → Release → Run workflow**, selecting this branch. A reviewer
approves the `pkg-release-approval` gate, then the RPM publishes to
Artifactory.
