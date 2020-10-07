<?php
$url = 'https://qa-orderapi.intelispend.com/Processes/IntelispendAPI/IntelispendOrderAPI/SubmitFileService.serviceagent?wsdl';
$opts = array(
    'http' => array(
        'verify_peer'       => false,
        'verify_peer_name'  => false
    )
);

$context = stream_context_create($opts);
$client = new SoapClient($url,
    array (
        "trace" => 1,
        "exception" => 1,
        'stream_context' => $context,
        'cache_wsdl' => WSDL_CACHE_NONE
    )
);

print_r( $client );


