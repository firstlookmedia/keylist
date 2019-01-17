# First Look Media Keylist

This repository contains an up-to-date list of PGP fingerprints that First Look employees use. The list is signed by the First Look Authority key. Here is the authority key:

```
pub   rsa4096/FD3ED09F 2016-02-17 [SC] [expires: 2017-02-16]
      Key fingerprint = 86EB 84C9 6B2E 6267 6B47  C491 9BB2 9FF9 FD3E D09F
      uid         [  full  ] First Look Authority
      sub   rsa4096/4F632ADB 2016-02-17 [E] [expires: 2017-02-16]
```

This will work with a [Keylist RFC](https://code.firstlook.media/keylist-rfc-explainer)-compatible client, like [GPG Sync](https://github.com/firstlookmedia/gpgsync). Use these values:

* Authority Key Fingerprint: `86EB84C96B2E62676B47C4919BB29FF9FD3ED09F`
* Keylist Address: `https://raw.githubusercontent.com/firstlookmedia/keylist/master/keylist.json`
