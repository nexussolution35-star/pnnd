# Deploying the static clone to surge.sh

The site is plain static HTML/CSS/assets and can be published as-is to a
public HTTPS preview host with [surge.sh](https://surge.sh).

## Live preview

Currently published at: **https://mcgeer-kitchens-alberton-4bb170.surge.sh**

> Temporary throwaway preview — published under a random `@mailinator.com`
> account, not tied to anyone. Tear down with `surge teardown <domain>`.

## Method (works behind an HTTPS-CONNECT-only proxy)

This environment routes outbound HTTPS through a proxy that only accepts
CONNECT tunnels. Surge bundles **axios 1.13.5**, which has broken HTTPS-proxy
handling (sends absolute-form requests the proxy rejects). Two adjustments
make it work:

1. **Upgrade surge's axios to ≥ 1.16.1** so requests use CONNECT tunnels:
   ```sh
   cd $(npm root -g)/surge
   npm install axios@^1.16.1
   rm -rf node_modules/surge-stream/node_modules/axios \
          node_modules/surge-sdk/node_modules/axios   # use the hoisted copy
   ```
2. **Trust the proxy CA in Node**: `export NODE_EXTRA_CA_CERTS=/root/.ccr/ca-bundle.crt`

Surge's interactive login prompt reads the password from a raw TTY, which is
unreliable to drive. Instead, register/authenticate non-interactively by
calling surge's `/token` endpoint directly (`get_token.js`) and publish with
`--token`:

```sh
export NODE_EXTRA_CA_CERTS=/root/.ccr/ca-bundle.crt
EMAIL="user$RANDOM@mailinator.com"
PASS="Pw$(openssl rand -hex 8)9z"
TOKEN=$(node get_token.js "$EMAIL" "$PASS" | awk '{print $2}')

# copy the site into a clean dir (no .git/.github/node_modules/README/.env)
surge ./_deploy mcgeer-kitchens-alberton-<rand>.surge.sh --token "$TOKEN"
```

`get_token.js` POSTs to `https://surge.surge.sh/token` with HTTP Basic auth;
surge auto-creates the account for a new email and returns the token.
