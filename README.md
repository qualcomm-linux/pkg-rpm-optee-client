# pkg-rpm-optee-client

This RPM packages [`OPTEE/optee_client`](https://github.com/OP-TEE/optee_client) with mink based changes
—  This package provides a Qualcomm-adapted build of the upstream OP-TEE PKCS#11
TEE client library (libckqteec), designed to communicate with the Qualcomm
Trusted Execution Environment (QTEE) via the MinkIPC transport layer.
It is based on the upstream OP-TEE Client source (https://github.com/OP-TEE/optee_client)
at version 4.0.0, with minimal patches applied to link against the Qualcomm
MinkIPC stack (libminkteec, libminkadaptor) instead of the standard OP-TEE transport.

This repo builds and publishes the Mink based `optee_client` RPM via the shared
[`qualcomm-linux/qcom-rpm-utils`](https://github.com/qualcomm-linux/qcom-rpm-utils)
reusable workflows — it follows the same one-package-per-repo template used
across `qualcomm-linux/pkg-rpm-*`.

## Branches

Following the Fedora/CentOS **dist-git** convention, each distro stream gets its
own branch, and the packaging files live at the branch root:

| Branch | Stream | Contents |
|---|---|---|
| `main` | — | Template docs, onboarding guide, community files. Nothing is built here. |
| **`c10s`** | CentOS 10 Stream | **This branch.** `mink-optee-client.spec` + `sources` + workflows. |

Full onboarding guide, configuration reference, and troubleshooting live on
[`main`](../../tree/main) — see its `README.md` and `docs/workflows.md`.

## Installation Instructions

```
sudo rpm -i mink-optee-client-x.aarch64.rpm
sudo rpm -i mink-optee-client-devel-x.aarch64.rpm
```

## Getting in Contact

How to contact maintainers. E.g. GitHub Issues, GitHub Discussions could be indicated for many cases. However a mail list or list of Maintainer e-mails could be shared for other types of discussions. E.g.

* [Report an Issue on GitHub](../../issues)
* [Open a Discussion on GitHub](../../discussions)

## License

pkg-rpm-optee-client is licensed under the [BSD-3-clause License](https://spdx.org/licenses/BSD-3-Clause.html). See [LICENSE.txt](LICENSE.txt) for the full license text.
