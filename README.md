# First Look Media Keylist

This repository contains an up-to-date list of PGP fingerprints that First Look employees use. The list is signed by the First Look Authority key. Here is the authority key:

```
pub   rsa4096 2016-02-17 [SC] [expires: 2020-02-16]
      86EB84C96B2E62676B47C4919BB29FF9FD3ED09F
uid           [  full  ] First Look Authority
sub   rsa4096 2016-02-17 [E] [expires: 2020-02-17]
sub   rsa4096 2017-04-12 [A] [expires: 2020-02-16]
```

This will work with a [Keylist RFC](https://code.firstlook.media/keylist-rfc-explainer)-compatible client, like [GPG Sync](https://github.com/firstlookmedia/gpgsync). Use these values:

* Authority Key Fingerprint: `86EB84C96B2E62676B47C4919BB29FF9FD3ED09F`
* Keylist Address: `https://raw.githubusercontent.com/firstlookmedia/keylist/master/keylist.json`
